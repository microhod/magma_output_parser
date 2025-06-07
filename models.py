from typing import Optional, Self
from dataclasses import dataclass

@dataclass
class GroupRepresentation:
    n: Optional[int]
    x: Optional[int]

    def __str__(self) -> str:
        if self.n is None and self.x is None:
            return "unknown"
        return f"<{self.n}:{self.x}>"

    def __hash__(self) -> int:
        return hash(str(self))
    
    def __eq__(self, other):
        return self.n == other.n and self.x == other.x
    
    def __lt__(self, other):
        # unknown groups are greater than non-unknowns
        if self.n is None and self.x is None:
            return False
        if other.n is None and other.x is None:
            return True

        return self.n < other.n or (self.n == other.n and self.x < other.x)


@dataclass
class GaloisInfo:
    type: GroupRepresentation
    nums: dict[str, int]


@dataclass
class Permutation:
    parts: list[tuple[int]]

    def __str__(self) -> str:
        s = ""
        for part in self.parts:
            s += '(' + ','.join([str(p) for p in part]) + ')'
        return s


@dataclass
class GroupPermutationRepresentation:
    perms: list[Permutation]

    def __str__(self) -> str:
        return '<' + ', '.join([str(p) for p in self.perms]) + '>'


@dataclass
class GroupStructure:
    properties: dict[str, dict[str, int]]
    soluble: Optional[bool] = None

    def zero(self) -> Self:
        return GroupStructure(
            soluble=self.soluble,
            properties={
                key: {prop: 0 for prop in properties}
                for key, properties in self.properties.items()
            }
        )
    
    def property_types(self) -> list[str]:
        return self.properties.keys()

    def property_keys(self, property_type: str) -> list[str]:
        return self.properties[property_type].keys()


@dataclass
class Group:
    perm_rep: GroupPermutationRepresentation
    isom_rep: GroupRepresentation
    structures: dict[GroupRepresentation, GroupStructure]
    galois: dict[str, list[GaloisInfo]]
    perm_id: Optional[int] = None
    soluble: Optional[bool] = None

    def order(self) -> int:
        rep = next(iter(self.structures.keys()))
        return rep.n

    def structure_property_types(self) -> list[str]:
        # all structures are assumed to have equal property types
        structure = next(iter(self.structures.values()))
        return structure.property_types()
    
    def structure_property_keys(self, property_type: str) -> list[str]:
        # all structures are assumed to have equal property keys, given the same type
        structure = next(iter(self.structures.values()))
        return structure.property_keys(property_type)



def normalise_group_structures(groups: list[Group]) -> list[Group]:
    structures = {rep: structure for g in groups for rep, structure in g.structures.items()}
    for g in groups:
        g.structures = {
            rep: g.structures[rep] if rep in g.structures else structure.zero()
            for rep, structure in structures.items()
        }
    return groups


def deduplicate_galois_infos(galois_infos: list[GaloisInfo]) -> list[GaloisInfo]:
    deduped = []
    seen_types = set()
    for info in galois_infos:
        if info.type in seen_types:
            continue

        seen_types.add(info.type)
        deduped.append(info)

    return deduped


# normalise_group_galois_types ensures all groups have the same galois types, with any missing types
# added in with zero'd GN values
def normalise_group_galois_types(groups: list[Group]) -> list[Group]:
    # sort groups by their isometry
    groups.sort(key=lambda g: g.isom_rep)

    for type in list(groups[0].galois.keys()):
        groups = _normalise_group_galois_types(groups, type)

    return groups

def _normalise_group_galois_types(groups: list[Group], galois_type: str) -> list[Group]:
    # get sorted list of all galois types and sort all group galois types
    # so they can be compared index by index
    galois_types = set()
    for group in groups:
        # galois can be duplicated, so we should remove duplicates
        group.galois[galois_type] = deduplicate_galois_infos(group.galois[galois_type])

        galois_types.update([galois.type for galois in group.galois[galois_type]])
        group.galois[galois_type].sort(key=lambda galois: galois.type)

    all_galois_types = list(galois_types)
    all_galois_types.sort()

    for group in groups:
        for i, type in enumerate(all_galois_types):
            if i < len(group.galois[galois_type]) and group.galois[galois_type][i].type == type:
                continue

            # we assume there is at least 1 galois info for each group.
            num_keys = list(group.galois[galois_type][0].nums.keys())

            # insert missing type with zero GN values at the correct index
            zero_galois = GaloisInfo(type=type, nums={key: 0 for key in num_keys})
            group.galois[galois_type] = group.galois[galois_type][:i] +[zero_galois] + group.galois[galois_type][i:]

    return groups

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

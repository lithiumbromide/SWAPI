---
title: "eDConfiguration Class"
project: ""
interface: "eDConfiguration"
member: ""
kind: "class"
source: "emodeltoolkit/eDConfiguration/eDConfiguration_Class.htm"
---

# eDConfiguration Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Creates assembly, part, animation, set of exploded sets, name of a material, mass properties, or hole properties.

#### Header file code

```vb
class eDConfiguration : public eDObject
{
public:

eDOutcome CreatePart( const ECHAR *partname, const eDAppearance &appearance, eDPart *& part ); //Creates a part

eDOutcome CreateAssembly( const ECHAR *assemblyname, const eDAppearance &appearance, eDAssembly *& assembly ); //Creates an assembly

eDOutcome CreateAnimation( const ECHAR *animationname, eDAnimation *& animation ); //Creates an animation

eDOutcome CreateExplode( bool isplayed, eDAnimation *& explode ); //Creates set of explode steps

eDOutcome SetMaterial( const ECHAR *material ); //Only sets the name; it is not associated with any material data, like mass

eDOutcome SetMassProperties( const eDMassProperties &massprops ); //Sets mass properties

eDOutcome AddHoleProperties( const eDHoleProperties &holeprops ); //Adds hole properties

};
```

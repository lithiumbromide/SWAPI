---
title: "eDMassProperties Class"
project: ""
interface: "eDMassProperties"
member: ""
kind: "class"
source: "emodeltoolkit/eDMassProperties/eDMassProperties_Class.htm"
---

# eDMassProperties Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains mass, volume, surface area, and center of gravity data. Use metric units (kg, m^3, m^3, m).

#### Header file code

```vb
class  eDMassProperties
{
public:

eDMassProperties( double mass, double volume, double area, const double cg[ 3 ] )
: _mass( mass ), _volume( volume ), _area( area )
{
_cg[ 0 ] = _cg[ 1 ] = _cg[ 2 ] = 0;
if ( cg )
{
_cg[ 0 ] = cg[ 0 ];
_cg[ 1 ] = cg[ 1 ];
_cg[ 2 ] = cg[ 2 ];
}
}
double GetMass() const { return _mass; }

double GetVolume() const { return _volume; }

double GetArea() const { return _area; }

void GetCG( double cg[ 3 ] ) const { cg[ 0 ] = _cg[ 0 ]; cg[ 1 ] = _cg[ 1 ]; cg[ 2 ] = _cg[ 2 ]; }

bool IsValid() const
{
return _mass > 0 || _volume > 0 || _area > 0;
};
};
```

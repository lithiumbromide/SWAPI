---
title: "eDTransform3d Class"
project: ""
interface: "eDTransform3d"
member: ""
kind: "class"
source: "emodeltoolkit/eDTransform3d/eDTransform3d_Class.htm"
---

# eDTransform3d Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents a 3D transform: translation, rotation, and scale.

#### Header file code

```vb
class eDTransform3d
{
public:

eDTransform3d();

eDTransform3d( const eDMatrix3d &m, const eDPt3d &v, double s = 1.0, bool rt = false, bool rf = false, bool sh = false );

eDTransform3d( const eDTransform3d &tr );

eDTransform3d( const eDPt3d &axis, double angle ); // Rotate by angle about axis

eDTransform3d( const eDPt3d &shift ); // Translate by shift

eDTransform3d( double scale );

const eDPt3d & translation() const;

const eDMatrix3d & affine() const;

double scale_factor() const;

void scale( double d );

eDPt3d apply_to_position( const eDPt3d & ) const;

eDPt3d apply_to_unitvec( const eDPt3d & ) const;

eDPt3d apply_to_vector( const eDPt3d & ) const;

double apply_to_scalar( double p ) const;

eDTransform3d inverse() const;

eDTransform3d mult( const eDTransform3d &t2 ) const;

bool is_shear() const;

bool is_rotate() const;

bool is_reflect() const;

bool is_identity() const;

bool is_isomorphic() const;

};
```

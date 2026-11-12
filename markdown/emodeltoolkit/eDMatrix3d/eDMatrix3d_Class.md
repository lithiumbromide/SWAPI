---
title: "eDMatrix3d Class"
project: ""
interface: "eDMatrix3d"
member: ""
kind: "class"
source: "emodeltoolkit/eDMatrix3d/eDMatrix3d_Class.htm"
---

# eDMatrix3d Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents a 3D rotation matrix.

#### Header file code

```vb
class eDMatrix3d
{
public:

eDMatrix3d();

eDMatrix3d( double xx, double xy, double xz, double yx, double yy, double yz, double zx, double zy, double zz );

eDMatrix3d( const eDPt3d &xv, const eDPt3d &yv, const eDPt3d &zv );

eDMatrix3d( const eDMatrix3d &p );

eDMatrix3d( const double p[9] );

double get_xx() const;

double get_xy() const;

double get_xz() const;

double get_yx() const;

double get_yy() const;

double get_yz() const;

double get_zx() const;

double get_zy() const;

double get_zz() const;

double operator[]( int i ) const;

double & operator[]( int i );

eDPt3d x_vec() const;

eDPt3d y_vec() const;

eDPt3d z_vec() const;

double determinant() const;

eDMatrix3d inverse();

eDMatrix3d normalize() const;

eDMatrix3d transpose() const;

eDMatrix3d mult( const eDMatrix3d &p ) const;

eDPt3d mult( const eDPt3d &v ) const;

eDMatrix3d mult( double d ) const;

};
```

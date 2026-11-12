---
title: "eDPt3d Class"
project: ""
interface: "eDPt3d"
member: ""
kind: "class"
source: "emodeltoolkit/eDPt3d/eDPt3d_Class.htm"
---

# eDPt3d Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents a point or vector in 3D space.

#### Header file code

```vb
class eDPt3d
{
public:

eDPt3d( double xc = 0, double yc = 0, double zc = 0 );

eDPt3d( const double c[ 3 ] );

eDPt3d( const eDPt3d & );

eDPt3d &operator=( const eDPt3d & );

double x() const;

double y() const;

double z() const;

void set_x( double t );

void set_y( double t );

void set_z( double t );

double operator[]( int i ) const;

double &operator[]( int i );

double norm() const;

eDPt3d normalize() const;

eDPt3d operator-();

eDPt3d &operator-=( const eDPt3d &p );

eDPt3d &operator+=( const eDPt3d &p );

eDPt3d &operator*=( double d );

eDPt3d &operator/=( double d );

bool coincident( const eDPt3d &p, double tol = POS_EPSILON ) const;

friend eDPt3d operator-( const eDPt3d &, const eDPt3d & );

friend eDPt3d operator+( const eDPt3d &, const eDPt3d & );

friend double operator%( const eDPt3d &, const eDPt3d & );

friend eDPt3d operator*( double, const eDPt3d & );

friend eDPt3d operator*( const eDPt3d &, double );

friend eDPt3d operator*( const eDPt3d &, const eDPt3d & );

friend eDPt3d operator/( const eDPt3d &, double );

};
```

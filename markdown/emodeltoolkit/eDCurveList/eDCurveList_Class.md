---
title: "eDCurveList Class"
project: ""
interface: "eDCurveList"
member: ""
kind: "class"
source: "emodeltoolkit/eDCurveList/eDCurveList_Class.htm"
---

# eDCurveList Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains one or more circles, arcs, ellipses, elliptical arcs, lines, polylines, individual polygons, and splines.

#### Header file code

```vb
class eDCurveList : public eDObject
{
public:

eDOutcome InsertLine( const eDPt3d &from, const eDPt3d &to, const eDLineStyle &style = eDLineStyle() ); //Inserts a line

eDOutcome InsertPolyline( int npoints, eDPt3d *pointdata, const eDLineStyle &style = eDLineStyle() ); //Inserts a polyline

eDOutcome InsertPolygon( int npoints, eDPt3d *pointdata, bool fill, const eDLineStyle &style = eDLineStyle() ); //Inserts a polygon

eDOutcome InsertCircle( const eDPt3d &start, const eDPt3d &mid, const eDPt3d &end, const eDLineStyle &style = eDLineStyle() ); //Inserts a circle

eDOutcome InsertCircularArc( const eDPt3d &start, const eDPt3d &mid, const eDPt3d &end, const eDLineStyle &style = eDLineStyle() ); //Inserts a circular arc

eDOutcome InsertEllipse( const eDPt3d ¢er, const eDPt3d &major, const eDPt3d &minor, const eDLineStyle &style = eDLineStyle() ); //Inserts an ellipse

eDOutcome InsertEllipticalArc( const eDPt3d ¢er, const eDPt3d &major, const eDPt3d &minor, double start, double end,const eDLineStyle &style = eDLineStyle() ); //Inserts an elliptical arc

eDOutcome InsertSpline( int degree, int npoints, eDPt3d *pointdata, float *weights, float *knots, const eDLineStyle &style = eDLineStyle() ); //Inserts a spline

eDOutcome InsertText( const ECHAR *text, const eDPt3d &insertpt, const eDFont &font, const eDPt3d *endpt = NULL, const eDLineStyle &style = eDLineStyle() ); //Inserts text

};
```

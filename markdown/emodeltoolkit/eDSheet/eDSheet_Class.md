---
title: "eDSheet Class"
project: ""
interface: "eDSheet"
member: ""
kind: "class"
source: "emodeltoolkit/eDSheet/eDSheet_Class.htm"
---

# eDSheet Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains one or more views.

#### Header file code

```vb
class eDSheet : public eDObject
{
public:

eDOutcome CreateBaseView( const ECHAR *viewname, eDView *& view ); //Creates a base view

eDOutcome CreateView( const ECHAR *viewname, const eDTransform3d &viewtransf, eDView *& view ); //Creates a view. The optional view transform argument will only position the view if it contains eDShellList geometry; that is, facet data added through eDBody::CreateShellList and added to a view through eDView::CreatePart. In all other instances, the view border will size automatically to hold other geometry (lines, points, curves, etc.) that are specified in global coordinates.

};
```

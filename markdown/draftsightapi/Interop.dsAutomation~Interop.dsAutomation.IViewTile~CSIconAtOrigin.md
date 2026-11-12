---
title: "CSIconAtOrigin Property (IViewTile)"
project: ""
interface: "IViewTile"
member: "CSIconAtOrigin"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewTile~CSIconAtOrigin.html"
---

# CSIconAtOrigin Property (IViewTile)

Gets or sets whether to display the coordinate system icon at the origin.

## Syntax

### Visual Basic

```vb
Property CSIconAtOrigin As System.Boolean
```

### C#

```csharp
System.bool CSIconAtOrigin {get; set;}
```

### JScript

```
function get,set CSIconAtOrigin : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_CSIconAtOrigin();
__property void set_CSIconAtOrigin(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool CSIconAtOrigin {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to display the coordinate system icon at the origin, false to not

## Examples

[Insert ViewTiles in Model (C#)](Insert_ViewTiles_in_Model_Example_CSharp.htm)
[Insert ViewTiles in Model (VB.NET)](Insert_ViewTiles_in_Model_Example_VBNET.htm)
[Insert ViewTiles in Model (VBA)](Insert_ViewTiles_in_Model_Example_VBA.htm)

## Remarks

To determine if the coordinate system icon is already displayed at the origin, call [IViewTile::CSIconIsOn](Interop.dsAutomation~Interop.dsAutomation.IViewTile~CSIconIsOn.html).

## See Also

[IViewTile Interface](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)
[IViewTile Members](Interop.dsAutomation~Interop.dsAutomation.IViewTile_members.html)
[IViewTile::CCSPerViewTile Property ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~CCSPerViewTile.html)

## Availability

DraftSight V1R6.0

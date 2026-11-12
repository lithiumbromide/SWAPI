---
title: "CSIconIsOn Property (IViewTile)"
project: ""
interface: "IViewTile"
member: "CSIconIsOn"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewTile~CSIconIsOn.html"
---

# CSIconIsOn Property (IViewTile)

Gets or sets whether the coordinate system icon is displayed at the origin.

## Syntax

### Visual Basic

```vb
Property CSIconIsOn As System.Boolean
```

### C#

```csharp
System.bool CSIconIsOn {get; set;}
```

### JScript

```
function get,set CSIconIsOn : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_CSIconIsOn();
__property void set_CSIconIsOn(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool CSIconIsOn {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the coordinate system icon is displayed at the origin, false if not

## Examples

[Insert ViewTiles in Model (C#)](Insert_ViewTiles_in_Model_Example_CSharp.htm)
[Insert ViewTiles in Model (VB.NET)](Insert_ViewTiles_in_Model_Example_VBNET.htm)
[Insert ViewTiles in Model (VBA)](Insert_ViewTiles_in_Model_Example_VBA.htm)

## Remarks

To display the coordinate system icon at the origin, call [IViewTile::CSIconAtOrigin](Interop.dsAutomation~Interop.dsAutomation.IViewTile~CSIconAtOrigin.html).

## See Also

[IViewTile Interface](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)
[IViewTile Members](Interop.dsAutomation~Interop.dsAutomation.IViewTile_members.html)
[IViewTile::CCSPerViewTile Property ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~CCSPerViewTile.html)

## Availability

DraftSight V1R6.0

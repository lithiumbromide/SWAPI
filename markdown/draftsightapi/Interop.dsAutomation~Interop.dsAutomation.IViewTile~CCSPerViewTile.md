---
title: "CCSPerViewTile Property (IViewTile)"
project: ""
interface: "IViewTile"
member: "CCSPerViewTile"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewTile~CCSPerViewTile.html"
---

# CCSPerViewTile Property (IViewTile)

Gets or sets whether the [custom coordinate system](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html) associated with this ViewTile becomes active when the ViewTile is [activated](Interop.dsAutomation~Interop.dsAutomation.IViewTile~ActivateView.html).

## Syntax

### Visual Basic

```vb
Property CCSPerViewTile As System.Boolean
```

### C#

```csharp
System.bool CCSPerViewTile {get; set;}
```

### JScript

```
function get,set CCSPerViewTile : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_CCSPerViewTile();
__property void set_CCSPerViewTile(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool CCSPerViewTile {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the custom coordinate system associated with this ViewTile becomes active when the ViewTile is activated, false if not

## See Also

[IViewTile Interface](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)
[IViewTile Members](Interop.dsAutomation~Interop.dsAutomation.IViewTile_members.html)
[IViewTile::Active Property ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~Active.html)
[IViewTile::CSIconAtOrigin Property ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~CSIconAtOrigin.html)
[IViewTile::CSIconIsOn Property ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~CSIconIsOn.html)

## Availability

DraftSight V1R6.0

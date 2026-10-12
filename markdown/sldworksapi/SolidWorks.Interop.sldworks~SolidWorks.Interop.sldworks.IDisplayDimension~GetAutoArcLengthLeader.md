---
title: "GetAutoArcLengthLeader Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetAutoArcLengthLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAutoArcLengthLeader.html"
---

# GetAutoArcLengthLeader Method (IDisplayDimension)

Gets whether the leader style of this arc-length dimension is being automatically selected or selected by the user.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutoArcLengthLeader() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetAutoArcLengthLeader()
```

### C#

```csharp
System.bool GetAutoArcLengthLeader()
```

### C++/CLI

```cpp
System.bool GetAutoArcLengthLeader();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the leader style is selected automatically , false if the leader style is selected by the user

## VBA Syntax

See [DisplayDimension::GetAutoArcLengthLeader](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetAutoArcLengthLeader.html).

## Remarks

The leader style of an arc-length dimension is specific to each display dimension. It can be parallel (the leaders are parallel to each other) or radial (the leaders are perpendicular to the extension line and would extend through the center of the arc). SOLIDWORKS can automatically select the style, or it can be specified by the user. Use IDisplayDimension::GetAutoArcLengthLeader to determine whether the leader type is selected automatically.

This method gets the leader style stored on this display dimension. If this display dimension is set to select the leader type automatically, then this method might return a value that is different from what is displayed.

This method applies to only arc length dimensions. It returns -1 if you run it on any other types of dimensions.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetArcLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArcLengthLeader.html)
[IDisplayDimension::SetArcLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArcLengthLeader.html)

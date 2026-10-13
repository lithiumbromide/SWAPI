---
title: "GetArcCentersDisplayed Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetArcCentersDisplayed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetArcCentersDisplayed.html"
---

# GetArcCentersDisplayed Method (IModelDoc2)

Gets whether the arc centers are displayed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcCentersDisplayed() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.GetArcCentersDisplayed()
```

### C#

```csharp
System.bool GetArcCentersDisplayed()
```

### C++/CLI

```cpp
System.bool GetArcCentersDisplayed();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if arc centers are currently displayed, false if not

## VBA Syntax

See [ModelDoc2::GetArcCentersDisplayed](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetArcCentersDisplayed.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetArcCentersDisplayed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetArcCentersDisplayed.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

---
title: "GetCurrentCoordinateSystemName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetCurrentCoordinateSystemName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCurrentCoordinateSystemName.html"
---

# GetCurrentCoordinateSystemName Method (IModelDoc2)

Gets the name of the current coordinate system or an empty string for the default coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentCoordinateSystemName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.String

value = instance.GetCurrentCoordinateSystemName()
```

### C#

```csharp
System.string GetCurrentCoordinateSystemName()
```

### C++/CLI

```cpp
System.String^ GetCurrentCoordinateSystemName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the current coordinate system

## VBA Syntax

See [ModelDoc2::GetCurrentCoordinateSystemName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetCurrentCoordinateSystemName.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.html)
[IModelDocExtension::GetCoordinateSystemTransformByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

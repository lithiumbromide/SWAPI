---
title: "GetImportedPath Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetImportedPath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetImportedPath.html"
---

# GetImportedPath Method (IComponent2)

Gets the full path name of the model imported for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImportedPath() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.GetImportedPath()
```

### C#

```csharp
System.string GetImportedPath()
```

### C++/CLI

```cpp
System.String^ GetImportedPath();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Full path name of the model imported for this component; empty string if model is not imported

## VBA Syntax

See [Component2::GetImportedPath](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetImportedPath.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPathName.html)
[IModelDoc2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.2

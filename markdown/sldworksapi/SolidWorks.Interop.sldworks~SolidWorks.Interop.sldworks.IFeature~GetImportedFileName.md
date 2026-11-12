---
title: "GetImportedFileName Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetImportedFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFileName.html"
---

# GetImportedFileName Method (IFeature)

Gets the file name from an imported feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImportedFileName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.String

value = instance.GetImportedFileName()
```

### C#

```csharp
System.string GetImportedFileName()
```

### C++/CLI

```cpp
System.String^ GetImportedFileName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

File name of the imported feature

## VBA Syntax

See [Feature::GetImportedFileName](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetImportedFileName.html).

## Remarks

This method applies only to imported features. All other features return an empty string. To get the type of this feature, use [IFeature::GetTypeName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::SetImportedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFileName.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

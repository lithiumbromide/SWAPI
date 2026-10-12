---
title: "SetImportedFileName Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetImportedFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFileName.html"
---

# SetImportedFileName Method (IFeature)

Sets the file name of an imported feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetImportedFileName( _
   ByVal ImpName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim ImpName As System.String
Dim value As System.Boolean

value = instance.SetImportedFileName(ImpName)
```

### C#

```csharp
System.bool SetImportedFileName(
   System.string ImpName
)
```

### C++/CLI

```cpp
System.bool SetImportedFileName(
   System.String^ ImpName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ImpName`: New filename of the imported feature

### Return Value

True if the filename was changed, false if not

## VBA Syntax

See [Feature::SetImportedFileName](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetImportedFileName.html).

## Remarks

This method applies only to imported features. To get the type of this feature, use [IFeature::GetTypeName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetImportedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFileName.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

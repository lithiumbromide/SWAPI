---
title: "SaveAsPreviousVersion Property (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "SaveAsPreviousVersion"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion.html"
---

# SaveAsPreviousVersion Property (IAdvancedSaveAsOptions)

Sets the SOLIDWORKS version to save to.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property SaveAsPreviousVersion As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions

instance.SaveAsPreviousVersion = value
```

### C#

```csharp
System.int SaveAsPreviousVersion {set;}
```

### C++/CLI

```cpp
property System.int SaveAsPreviousVersion {
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

SOLIDWORKS version to save to (see **Remarks**)

## VBA Syntax

See [AdvancedSaveAsOptions::SaveAsPreviousVersion](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~SaveAsPreviousVersion.html).

## Examples

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html) example.

## Remarks

Examine the Remarks of [ISldWorks::VersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.html) to find the SOLIDWORKS version to save to.

For this property to save a model as a previous version, you must also use [IAdvancedSaveAsOptions::ModifyItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.html) to change the name/path of all of the model's references. You must provide a different name/path than the current name/path, otherwise the SaveAs operation may fail because overwriting the same file is not supported.

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32

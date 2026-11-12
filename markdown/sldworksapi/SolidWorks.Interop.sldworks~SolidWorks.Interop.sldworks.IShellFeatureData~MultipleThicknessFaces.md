---
title: "MultipleThicknessFaces Property (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "MultipleThicknessFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.html"
---

# MultipleThicknessFaces Property (IShellFeatureData)

Gets and sets the multiple-thickness faces in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MultipleThicknessFaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim value As System.Object

instance.MultipleThicknessFaces = value

value = instance.MultipleThicknessFaces
```

### C#

```csharp
System.object MultipleThicknessFaces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MultipleThicknessFaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of multiple-thickness [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [ShellFeatureData::MultipleThicknessFaces](ms-its:sldworksapivb6.chm::/sldworks~ShellFeatureData~MultipleThicknessFaces.html).

## Examples

See the [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::GetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessAtIndex.html)
[IShellFeatureData::GetMultipleThicknessFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessFacesCount.html)
[IShellFeatureData::IGetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetMultipleThicknessFaces.html)
[IShellFeatureData::ISetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetMultipleThicknessFaces.html)
[IShellFeatureData::SetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~SetMultipleThicknessAtIndex.html)
[IShellFeatureData::MultipleThicknessFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.html)
[IShellFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Thickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

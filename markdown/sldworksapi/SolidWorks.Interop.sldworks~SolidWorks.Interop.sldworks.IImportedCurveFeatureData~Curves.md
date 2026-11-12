---
title: "Curves Property (IImportedCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IImportedCurveFeatureData"
member: "Curves"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~Curves.html"
---

# Curves Property (IImportedCurveFeatureData)

Gets or sets the curves for this imported curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Curves As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IImportedCurveFeatureData
Dim value As System.Object

instance.Curves = value

value = instance.Curves
```

### C#

```csharp
System.object Curves {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Curves {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of curves (see **Remarks**)

## VBA Syntax

See [ImportedCurveFeatureData::Curves](ms-its:sldworksapivb6.chm::/sldworks~ImportedCurveFeatureData~Curves.html).

## Remarks

The curve feature is formed in the order of the input curves.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IImportedCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.html)
[IImportedCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.html)
[IImportedCurveFeatureData::GetCurveCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~GetCurveCount.html)
[IImportedCurveFeatureData::IGetCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~IGetCurves.html)
[IImportedCurveFeatureData::ISetCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~ISetCurves.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

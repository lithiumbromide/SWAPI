---
title: "GetContoursCount Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "GetContoursCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetContoursCount.html"
---

# GetContoursCount Method (IRevolveFeatureData2)

Gets the number of selected contours for this revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetContoursCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim value As System.Integer

value = instance.GetContoursCount()
```

### C#

```csharp
System.int GetContoursCount()
```

### C++/CLI

```cpp
System.int GetContoursCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of selected contours

## VBA Syntax

See [RevolveFeatureData2::GetContoursCount](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~GetContoursCount.html).

## Remarks

This method returns the total number of sketch contours and sketch regions used in the base sketch for this feature.

Call this method before calling [IRevolveFeatureData2::IGetContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~IGetContours.html) to get the size of the array for that method.

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetContours.html)
[IRevolveFeatureData2::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Contours.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

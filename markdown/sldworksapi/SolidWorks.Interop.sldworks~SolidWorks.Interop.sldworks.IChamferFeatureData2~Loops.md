---
title: "Loops Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "Loops"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Loops.html"
---

# Loops Property (IChamferFeatureData2)

Gets and sets the loops to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Property Loops As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Object

instance.Loops = value

value = instance.Loops
```

### C#

```csharp
System.object Loops {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Loops {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of chamfered [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html)

## VBA Syntax

See [ChamferFeatureData2::Loops](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~Loops.html).

## Examples

[Get Chamfer Distances (C#)](Get_Chamfer_Distances_Example_CSharp.htm)
[Get Chamfer Distances (VB.NET)](Get_Chamfer_Distances_Example_VBNET.htm)
[Get Chamfer Distances (VBA)](Get_Chamfer_Distances_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::IGetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetLoops.html)
[IChamferFeatureData2::ISetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetLoops.html)
[IChamferFeatureData2::LoopCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~LoopCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

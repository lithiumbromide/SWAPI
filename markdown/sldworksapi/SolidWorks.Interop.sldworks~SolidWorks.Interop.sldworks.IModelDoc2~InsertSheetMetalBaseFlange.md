---
title: "InsertSheetMetalBaseFlange Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSheetMetalBaseFlange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalBaseFlange.html"
---

# InsertSheetMetalBaseFlange Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertSheetMetalBaseFlange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSheetMetalBaseFlange( _
   ByVal Thickness As System.Double, _
   ByVal ThickenDir As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal ExtrudeDist1 As System.Double, _
   ByVal ExtrudeDist2 As System.Double, _
   ByVal FlipExtruDir As System.Boolean, _
   ByVal EndCondition1 As System.Integer, _
   ByVal EndCondition2 As System.Integer, _
   ByVal DirToUse As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim ThickenDir As System.Boolean
Dim Radius As System.Double
Dim ExtrudeDist1 As System.Double
Dim ExtrudeDist2 As System.Double
Dim FlipExtruDir As System.Boolean
Dim EndCondition1 As System.Integer
Dim EndCondition2 As System.Integer
Dim DirToUse As System.Integer

instance.InsertSheetMetalBaseFlange(Thickness, ThickenDir, Radius, ExtrudeDist1, ExtrudeDist2, FlipExtruDir, EndCondition1, EndCondition2, DirToUse)
```

### C#

```csharp
void InsertSheetMetalBaseFlange(
   System.double Thickness,
   System.bool ThickenDir,
   System.double Radius,
   System.double ExtrudeDist1,
   System.double ExtrudeDist2,
   System.bool FlipExtruDir,
   System.int EndCondition1,
   System.int EndCondition2,
   System.int DirToUse
)
```

### C++/CLI

```cpp
void InsertSheetMetalBaseFlange(
   System.double Thickness,
   System.bool ThickenDir,
   System.double Radius,
   System.double ExtrudeDist1,
   System.double ExtrudeDist2,
   System.bool FlipExtruDir,
   System.int EndCondition1,
   System.int EndCondition2,
   System.int DirToUse
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:
- `ThickenDir`:
- `Radius`:
- `ExtrudeDist1`:
- `ExtrudeDist2`:
- `FlipExtruDir`:
- `EndCondition1`:
- `EndCondition2`:
- `DirToUse`:

## VBA Syntax

See [ModelDoc2::InsertSheetMetalBaseFlange](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSheetMetalBaseFlange.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

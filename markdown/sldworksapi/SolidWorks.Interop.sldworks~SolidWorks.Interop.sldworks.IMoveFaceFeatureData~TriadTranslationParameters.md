---
title: "TriadTranslationParameters Property (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "TriadTranslationParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadTranslationParameters.html"
---

# TriadTranslationParameters Property (IMoveFaceFeatureData)

Gets or sets the translation parameters for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TriadTranslationParameters As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim value As System.Object

instance.TriadTranslationParameters = value

value = instance.TriadTranslationParameters
```

### C#

```csharp
System.object TriadTranslationParameters {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TriadTranslationParameters {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of three doubles, which are the X, Y, and Z translation parameters

## VBA Syntax

See [MoveFaceFeatureData::TriadTranslationParameters](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~TriadTranslationParameters.html).

## Examples

[Translate Move Face Feature (VB.NET)](Translate_Move_Face_Feature_Example_VBNET.htm)
[Translate Move Face Feature (VBA)](Translate_Move_Face_Feature_Example_VB.htm)
[Translate Move Face Feature (C#)](Translate_Move_Face_Feature_Example_CSharp.htm)
[Create and Modify Move Face Feature (C#)](Create_and_Modify_Move_Face_Feature_Example_CSharp.htm)

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::IGetTriadTranslationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadTranslationParameters.html)
[IMoveFaceFeatureData::ISetTriadTranslationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadTranslationParameters.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

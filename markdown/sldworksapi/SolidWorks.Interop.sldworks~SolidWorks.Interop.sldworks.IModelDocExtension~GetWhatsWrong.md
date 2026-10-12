---
title: "GetWhatsWrong Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetWhatsWrong"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrong.html"
---

# GetWhatsWrong Method (IModelDocExtension)

Gets the What's Wrong dialog information for this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWhatsWrong( _
   ByRef Features As System.Object, _
   ByRef ErrorCodes As System.Object, _
   ByRef Warnings As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Features As System.Object
Dim ErrorCodes As System.Object
Dim Warnings As System.Object
Dim value As System.Boolean

value = instance.GetWhatsWrong(Features, ErrorCodes, Warnings)
```

### C#

```csharp
System.bool GetWhatsWrong(
   out System.object Features,
   out System.object ErrorCodes,
   out System.object Warnings
)
```

### C++/CLI

```cpp
System.bool GetWhatsWrong(
   [Out] System.Object^ Features,
   [Out] System.Object^ ErrorCodes,
   [Out] System.Object^ Warnings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Features`: Array of features in the What's Wrong dialog
- `ErrorCodes`: Array of error codes corresponding to the features in the What's Wrong dialog as defined in [swFeatureError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)
- `Warnings`: Array of Booleans corresponding to the features in the What's Wrong dialog indicating whether SOLIDWORKS detected a What's Wrong item as a warning; true if SOLIDWORKS detected a What's Wrong item as a warning, false if not

### Return Value

True if this method runs successfully, false if not

## VBA Syntax

See [ModelDocExtension::GetWhatsWrong](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetWhatsWrong.html).

## Examples

[Get What's Wrong (C#)](Get_What's_Wrong_Example_CSharp.htm)
[Get What's Wrong (VB.NET)](Get_What's_Wrong_Example_VBNET.htm)
[Get What's Wrong (VBA)](Get_What's_Wrong_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetWhatsWrongCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrongCount.html)
[IFeature::GetErrorCode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.html)
[IMacroFeatureData::Provider Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider.html)

## Availability

SOLIDWORKS 2009 SP3, Revision Number 17.3

---
title: "GetErrorCode2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetErrorCode2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.html"
---

# GetErrorCode2 Method (IFeature)

Gets the error code for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetErrorCode2( _
   ByRef IsWarning As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim IsWarning As System.Boolean
Dim value As System.Integer

value = instance.GetErrorCode2(IsWarning)
```

### C#

```csharp
System.int GetErrorCode2(
   out System.bool IsWarning
)
```

### C++/CLI

```cpp
System.int GetErrorCode2(
   [Out] System.bool IsWarning
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IsWarning`: True if the error is a warning, false if not

  **NOTE**: This parameter should only be examined if the return value is non-zero.

### Return Value

Feature error code as defined in [swFeatureError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)

## VBA Syntax

See [Feature::GetErrorCode2](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetErrorCode2.html).

## Examples

[Get Error Codes for Features (VBA)](Get_Error_Codes_for_Features_Example_VB.htm)

## Remarks

This method returns many of the errors indicated by the What's Wrong icon seen with an invalid feature in the FeatureManager design tree.

During feature creation, you can prevent the error dialog from appearing by using
[IModelDoc2::ShowFeatureErrorDialog](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[ISldWorks::AllowFailedFeatureCreation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AllowFailedFeatureCreation.html)
[IModelDoc2::ShowFeatureErrorDialog Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.html)
[IModelDocExtension::GetWhatsWrong Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrong.html)
[IModelDocExtension::GetWhatsWrongCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrongCount.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

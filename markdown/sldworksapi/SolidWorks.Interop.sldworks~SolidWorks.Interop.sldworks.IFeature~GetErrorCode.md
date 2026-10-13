---
title: "GetErrorCode Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetErrorCode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode.html"
---

# GetErrorCode Method (IFeature)

Obsolete. Superseded by [IFeature::GetErrorCode2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetErrorCode2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetErrorCode() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.GetErrorCode()
```

### C#

```csharp
System.int GetErrorCode()
```

### C++/CLI

```cpp
System.int GetErrorCode();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Feature error code as defined in [swFeatureError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)

## VBA Syntax

See [Feature::GetErrorCode](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetErrorCode.html).

## Remarks

This method returns many of the errors indicated by the "What's Wrong" icon seen with an invalid feature in the FeatureManager design tree.

During feature creation, you can prevent the error dialog from appearing by using
[IModelDoc2::ShowFeatureErrorDialog](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

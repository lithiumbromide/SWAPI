---
title: "AllowFailedFeatureCreation Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AllowFailedFeatureCreation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AllowFailedFeatureCreation.html"
---

# AllowFailedFeatureCreation Method (ISldWorks)

Sets whether to allow the creation of a feature that has rebuild errors.

## Syntax

### Visual Basic (Declaration)

```vb
Function AllowFailedFeatureCreation( _
   ByVal YesNo As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim YesNo As System.Boolean
Dim value As System.Boolean

value = instance.AllowFailedFeatureCreation(YesNo)
```

### C#

```csharp
System.bool AllowFailedFeatureCreation(
   System.bool YesNo
)
```

### C++/CLI

```cpp
System.bool AllowFailedFeatureCreation(
   System.bool YesNo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `YesNo`: True if features are to be created regardless of rebuild errors, false if not

### Return Value

The previous value, which is now replaced by the value for YesNo

## VBA Syntax

See [SldWorks::AllowFailedFeatureCreation](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AllowFailedFeatureCreation.html).

## Examples

[Create Feature With Invalid Geometry (VBA)](Create_Feature_with_Invalid_Geometry_Example_VB.htm)

## Remarks

By default, features are not created when invalid geometry is specified; however, after calling this method with YesNo set to True, the features are created but with rebuild errors.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

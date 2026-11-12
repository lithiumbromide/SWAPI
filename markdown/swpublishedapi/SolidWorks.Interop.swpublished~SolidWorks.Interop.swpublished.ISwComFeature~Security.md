---
title: "Security Method (ISwComFeature)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwComFeature"
member: "Security"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature~Security.html"
---

# Security Method (ISwComFeature)

Allows you to specify whether instances of the macro feature created using COM can be rolled back, edited, suppressed, replaced, or deleted from the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function Security( _
   ByVal app As System.Object, _
   ByVal modelDoc As System.Object, _
   ByVal feature As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwComFeature
Dim app As System.Object
Dim modelDoc As System.Object
Dim feature As System.Object
Dim value As System.Object

value = instance.Security(app, modelDoc, feature)
```

### C#

```csharp
System.object Security(
   System.object app,
   System.object modelDoc,
   System.object feature
)
```

### C++/CLI

```cpp
System.Object^ Security(
   System.Object^ app,
   System.Object^ modelDoc,
   System.Object^ feature
)
```

### Parameters

- `app`: SOLIDWORKS application
- `modelDoc`: SOLIDWORKS document in which the macro feature appears
- `feature`: Macro feature whose security you want to set

### Return Value

Value or combination of values as defined by [swMacroFeatureSecurityOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureSecurityOptions_e.html)

## VBA Syntax

See [SwComFeature::Security](ms-its:swpublishedapivb6.chm::/swpublished~SwComFeature~Security.html).

## Remarks

This method also allows you to display a note associated with the macro feature to the end user. This method is required for COM-based macro features. See [Overview of Macro Features](sldworksAPIProgGuide.chm::/Macro_Features/Overview_of_Macro_Features.htm) for more information.

## See Also

[ISwComFeature Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature.html)
[ISwComFeature Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

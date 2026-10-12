---
title: "ReferencedFeatures Method (ISwDMExternalReferenceOption2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMExternalReferenceOption2"
member: "ReferencedFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2~ReferencedFeatures.html"
---

# ReferencedFeatures Method (ISwDMExternalReferenceOption2)

Gets the names and types of reference features in the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReferencedFeatures( _
   ByRef FeatureNames As System.Object, _
   ByRef FeatureTypes As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMExternalReferenceOption2
Dim FeatureNames As System.Object
Dim FeatureTypes As System.Object
Dim value As System.Boolean

value = instance.ReferencedFeatures(FeatureNames, FeatureTypes)
```

### C#

```csharp
System.bool ReferencedFeatures(
   out System.object FeatureNames,
   out System.object FeatureTypes
)
```

### C++/CLI

```cpp
System.bool ReferencedFeatures(
   [Out] System.Object^ FeatureNames,
   [Out] System.Object^ FeatureTypes
)
```

### Parameters

- `FeatureNames`: Array of strings of the names of the referenced features
- `FeatureTypes`: Array of strings of the types of referenced features

### Return Value

True if the method successfully executes, false if the method fails to execute

## VBA Syntax

See [SwDMExternalReferenceOption2::ReferencedFeatures](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMExternalReferenceOption2~ReferencedFeatures.html).

## Examples

[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

## See Also

[ISwDMExternalReferenceOption2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.html)
[ISwDMExternalReferenceOption2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2_members.html)

## Availability

SOLIDWORKS Document Manager API 2014 SP0

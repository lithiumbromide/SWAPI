---
title: "HasLegacyCustomProperties Property (ISwDMDocument29)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument29"
member: "HasLegacyCustomProperties"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29~HasLegacyCustomProperties.html"
---

# HasLegacyCustomProperties Property (ISwDMDocument29)

Gets whether this document has legacy custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasLegacyCustomProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument29
Dim value As System.Boolean

value = instance.HasLegacyCustomProperties
```

### C#

```csharp
System.bool HasLegacyCustomProperties {get;}
```

### C++/CLI

```cpp
property System.bool HasLegacyCustomProperties {
   System.bool get();
}
```

### Property Value

True if document has legacy custom properties, false if not

## VBA Syntax

See [SwDMDocument29::HasLegacyCustomProperties](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument29~HasLegacyCustomProperties.html).

## See Also

[ISwDMDocument29 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29.html)
[ISwDMDocument29 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29_members.html)

## Availability

SOLIDWORKS Document Manager API 2023 FCS

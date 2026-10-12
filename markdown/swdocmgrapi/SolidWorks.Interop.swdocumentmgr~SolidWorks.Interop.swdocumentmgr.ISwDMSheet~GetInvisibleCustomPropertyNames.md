---
title: "GetInvisibleCustomPropertyNames Method (ISwDMSheet)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSheet"
member: "GetInvisibleCustomPropertyNames"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyNames.html"
---

# GetInvisibleCustomPropertyNames Method (ISwDMSheet)

Gets the names of this sheet's invisible custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInvisibleCustomPropertyNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSheet
Dim value As System.Object

value = instance.GetInvisibleCustomPropertyNames()
```

### C#

```csharp
System.object GetInvisibleCustomPropertyNames()
```

### C++/CLI

```cpp
System.Object^ GetInvisibleCustomPropertyNames();
```

### Return Value

Array of strings of the names of the invisible custom properties for this sheet

## VBA Syntax

See [SwDMSheet::GetInvisibleCustomPropertyNames](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSheet~GetInvisibleCustomPropertyNames.html).

## Remarks

Before calling this method, call [ISwDMSheet::GetInvisibleCustomPropertyCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyCount.html) to determine the size of the array.

Call this method before calling [ISwDMSheet::GetInvisibleCustomProperty](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomProperty.html) to determine the name of the invisible custom property you want to use with that method.

## See Also

[ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.html)
[ISwDMSheet Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0

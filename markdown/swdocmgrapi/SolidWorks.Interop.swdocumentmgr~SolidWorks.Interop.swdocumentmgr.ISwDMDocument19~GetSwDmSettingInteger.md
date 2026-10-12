---
title: "GetSwDmSettingInteger Method (ISwDMDocument19)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument19"
member: "GetSwDmSettingInteger"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~GetSwDmSettingInteger.html"
---

# GetSwDmSettingInteger Method (ISwDMDocument19)

Gets the specified document setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSwDmSettingInteger( _
   ByVal DmSetting As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument19
Dim DmSetting As System.Integer
Dim value As System.Integer

value = instance.GetSwDmSettingInteger(DmSetting)
```

### C#

```csharp
System.int GetSwDmSettingInteger(
   System.int DmSetting
)
```

### C++/CLI

```cpp
System.int GetSwDmSettingInteger(
   System.int DmSetting
)
```

### Parameters

- `DmSetting`: Setting as defined by [swDmDocumentUnitsIntegerValue_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDocumentUnitsIntegerValue_e.html)

### Return Value

Value for DmSetting

## VBA Syntax

See [SwDMDocument19::GetSwDmSettingInteger](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument19~GetSwDmSettingInteger.html).

## Examples

See the [ISwDMDocument19](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html) examples.

## Remarks

This method works only with documents saved in SOLIDWORKS 2015 or later.

## See Also

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.html)
[ISwDMDocument19::GetSwDmSettingToggle Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~GetSwDmSettingToggle.html)

## Availability

SOLIDWORKS Document Manager API 2015 SP0

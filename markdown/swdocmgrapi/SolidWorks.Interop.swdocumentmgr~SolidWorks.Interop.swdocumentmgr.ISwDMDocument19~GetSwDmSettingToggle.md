---
title: "GetSwDmSettingToggle Method (ISwDMDocument19)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument19"
member: "GetSwDmSettingToggle"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~GetSwDmSettingToggle.html"
---

# GetSwDmSettingToggle Method (ISwDMDocument19)

Gets the specified document setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSwDmSettingToggle( _
   ByVal DmSetting As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument19
Dim DmSetting As System.Integer
Dim value As System.Boolean

value = instance.GetSwDmSettingToggle(DmSetting)
```

### C#

```csharp
System.bool GetSwDmSettingToggle(
   System.int DmSetting
)
```

### C++/CLI

```cpp
System.bool GetSwDmSettingToggle(
   System.int DmSetting
)
```

### Parameters

- `DmSetting`: Setting as defined by [swDmDocumentUnitsToggle_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDocumentUnitsToggle_e.html)

### Return Value

Value for DmSetting

## VBA Syntax

See [SwDMDocument19::GetSwDmSettingToggle](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument19~GetSwDmSettingToggle.html).

## Examples

See the [ISwDMDocument19](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html) examples.

## Remarks

This method works only with documents saved in SOLIDWORKS 2015 or later.

## See Also

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.html)
[ISwDMDocument19::GetSwDmSettingInteger Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~GetSwDmSettingInteger.html)

## Availability

SOLIDWORKS Document Manager API 2015 SP0

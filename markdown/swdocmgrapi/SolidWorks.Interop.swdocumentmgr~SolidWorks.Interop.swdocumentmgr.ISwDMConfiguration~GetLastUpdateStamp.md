---
title: "GetLastUpdateStamp Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "GetLastUpdateStamp"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetLastUpdateStamp.html"
---

# GetLastUpdateStamp Method (ISwDMConfiguration)

Gets the date that this configuration was last updated.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastUpdateStamp() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim value As System.Integer

value = instance.GetLastUpdateStamp()
```

### C#

```csharp
System.int GetLastUpdateStamp()
```

### C++/CLI

```cpp
System.int GetLastUpdateStamp();
```

### Return Value

Date last updated

## VBA Syntax

See [SwDMConfiguration::GetLastUpdateStamp](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~GetLastUpdateStamp.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

The update stamp is essentially an integer form of a time stamp. The update stamp in a SOLIDWORKS document is incremented when:

- the state of the model changes (for example, you suppress or unsuppress a feature in a part or an assembly)
- the geometry changes (for example, any action that requires a rebuild)

This time stamp is not incremented for such operations as color changes, feature or configuration name changes, and so on.

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS

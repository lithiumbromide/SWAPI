---
title: "GetID Method (ISwDMConfiguration12)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration12"
member: "GetID"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetID.html"
---

# GetID Method (ISwDMConfiguration12)

Gets the ID of the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration12
Dim value As System.Integer

value = instance.GetID()
```

### C#

```csharp
System.int GetID()
```

### C++/CLI

```cpp
System.int GetID();
```

### Return Value

ID of the configuration

## VBA Syntax

See [SwDMConfiguration12::GetID](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration12~GetID.html).

## Examples

[Get Linked Display States (C#)](Get_Linked_Display_States_Example_CSharp.htm)
[Get Linked Display States (VB.NET)](Get_Linked_Display_States_Example_VBNET.htm)

## Remarks

Each configuration is assigned a unique and persistent ID. This ID does not change if you change the name of the configuration.

## See Also

[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.html)
[ISwDMConfiguration12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

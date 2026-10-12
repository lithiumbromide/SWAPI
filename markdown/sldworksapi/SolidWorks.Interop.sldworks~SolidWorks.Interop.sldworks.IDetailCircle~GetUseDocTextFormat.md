---
title: "GetUseDocTextFormat Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetUseDocTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetUseDocTextFormat.html"
---

# GetUseDocTextFormat Method (IDetailCircle)

Gets whether or not SOLIDWORKS is currently using the document default setting for text format.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocTextFormat() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Boolean

value = instance.GetUseDocTextFormat()
```

### C#

```csharp
System.bool GetUseDocTextFormat()
```

### C++/CLI

```cpp
System.bool GetUseDocTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if SOLIDWORKS is using the default settings for the text format, false if not

## VBA Syntax

See [DetailCircle::GetUseDocTextFormat](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetUseDocTextFormat.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetTextFormat.html)
[IDetailCircle::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetTextFormat.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

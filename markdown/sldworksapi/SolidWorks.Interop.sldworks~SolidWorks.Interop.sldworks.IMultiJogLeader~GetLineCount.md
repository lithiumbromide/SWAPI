---
title: "GetLineCount Method (IMultiJogLeader)"
project: "SOLIDWORKS API Help"
interface: "IMultiJogLeader"
member: "GetLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetLineCount.html"
---

# GetLineCount Method (IMultiJogLeader)

Gets the number of line items in this multi-jog leader.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMultiJogLeader
Dim value As System.Integer

value = instance.GetLineCount()
```

### C#

```csharp
System.int GetLineCount()
```

### C++/CLI

```cpp
System.int GetLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of line items

## VBA Syntax

See [MultiJogLeader::GetLineCount](ms-its:sldworksapivb6.chm::/sldworks~MultiJogLeader~GetLineCount.html).

## Examples

[Get Multi-jog Leader Data (C#)](Get_Multi-jog_Leader_Data_Example_CSharp.htm)
[Get Multi-jog Leader Data (VB.NET)](Get_Multi-jog_Leader_Data_Example_VBNET.htm)
[Get Multi-jog Leader Data (VBA)](Get_Multi-jog_Leader_Data_Example_VB.htm)

## See Also

[IMultiJogLeader Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.html)
[IMultiJogLeader Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader_members.html)
[IMultiJogLeader::GetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetLineAtIndex.html)
[IMultiJogLeader::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetLineAtIndex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

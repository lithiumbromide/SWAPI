---
title: "GetProcess Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetProcess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetProcess.html"
---

# GetProcess Method (IWeldSymbol)

Gets whether the indication of welding process flag is set on this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProcess() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim value As System.Boolean

value = instance.GetProcess()
```

### C#

```csharp
System.bool GetProcess()
```

### C++/CLI

```cpp
System.bool GetProcess();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the indication of welding process flag is set, false if not

## VBA Syntax

See [WeldSymbol::GetProcess](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetProcess.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

Get:

- Text related to the indication of welding process using [IWeldSymbol::GetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetText.html).
- Flag that indicates whether a reference box exists around this text using [IWeldSymbol::GetProcessReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetProcessReference.html).

Set all of the indication of welding process values (flag, text, and reference) using [IWeldSymbol::SetProcess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetProcess.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.html)

## Availability

SOLIDWORKS 99, datecode 1999207

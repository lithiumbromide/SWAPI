---
title: "GetProcessReference Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetProcessReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetProcessReference.html"
---

# GetProcessReference Method (IWeldSymbol)

Gets whether there is a reference box around the indication of welding process text.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProcessReference() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim value As System.Boolean

value = instance.GetProcessReference()
```

### C#

```csharp
System.bool GetProcessReference()
```

### C++/CLI

```cpp
System.bool GetProcessReference();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if there is a reference box around the process text, false if not

## VBA Syntax

See [WeldSymbol::GetProcessReference](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetProcessReference.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

Get:

- Flag that tells whether or not the indication of welding process flag is set on this weld symbol using [IWeldSymbol::GetProcess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetProcess.html).
- Text related to the indication of welding process using [IWeldSymbol::GetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetText.html).

Set all of the indication of welding process values (flag, text, and reference) using [IWeldSymbol::SetProcess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetProcess.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.html)

## Availability

SOLIDWORKS 99, datecode 1999207

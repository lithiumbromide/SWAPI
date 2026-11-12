---
title: "SetProcess Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "SetProcess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetProcess.html"
---

# SetProcess Method (IWeldSymbol)

Sets the values related to the indication of welding process for this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetProcess( _
   ByVal Process As System.Boolean, _
   ByVal Text As System.String, _
   ByVal Reference As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Process As System.Boolean
Dim Text As System.String
Dim Reference As System.Boolean
Dim value As System.Boolean

value = instance.SetProcess(Process, Text, Reference)
```

### C#

```csharp
System.bool SetProcess(
   System.bool Process,
   System.string Text,
   System.bool Reference
)
```

### C++/CLI

```cpp
System.bool SetProcess(
   System.bool Process,
   System.String^ Text,
   System.bool Reference
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Process`: True to set the indication of welding process flag, false to not
- `Text`: Text related to the indication of welding process
- `Reference`: True to place a reference box around the process text, false to not

### Return Value

True if the indication of welding process is set, false if not

## VBA Syntax

See [WeldSymbol::SetProcess](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~SetProcess.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

Get:

- Flag that indicates whether the indication of welding process flag is set on this weld symbol using [IWeldSymbol::GetProcess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetProcess.html).

- Text related to the indication of welding process using [IWeldSymbol::GetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetText.html).
- Flag that indicates whether a reference box exists around this text using [IWeldSymbol::GetProcessReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetProcessReference.html).

The text and reference box are visible if Process is true.

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.html)

## Availability

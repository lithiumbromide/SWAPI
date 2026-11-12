---
title: "IEnvironment Interface"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html"
---

# IEnvironment Interface

Allows you to analyze the text and geometry used to create a geometric tolerance symbol.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IEnvironment
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
```

### C#

```csharp
public interface IEnvironment
```

### C++/CLI

```cpp
public interface class IEnvironment
```

## VBA Syntax

See [Environment](ms-its:sldworksapivb6.chm::/sldworks~Environment.html).

## Examples

[Analyze Text and Geometry in GTol Symbol (C#)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_CSharp.htm)
[Analyze Text and Geometry in GTol Symbol (VB.NET)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VBNET.htm)
[Analyze Text and Geometry in GTol Symbol (VBA)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VB.htm)

## Remarks

This interface can be useful if you have a note that contains a geometric tolerance symbol and you want to translate that note.

You can find the file containing the list of supported geometric tolerance symbols and their abbreviations in **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym****.**

**NOTE:** All numeric values returned from IEnvironment are relative to a unit text height of 1.0; i.e., if a geometric tolerance symbol has a text height of 0.15, then multiply the numeric values returned by 0.15.

## Accessors

[ISldWorks::GetEnvironment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetEnvironment.html) and [ISldWorks::IGetEnvironment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetEnvironment.html)

## Access Diagram

[Environment](SWObjectModel.pdf#Environment)

## See Also

[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

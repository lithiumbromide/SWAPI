---
title: "SetTextFormat Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "SetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~SetTextFormat.html"
---

# SetTextFormat Method (ISketchText)

Sets the text format for this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTextFormat( _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim UseDoc As System.Boolean
Dim TextFormat As System.Object
Dim value As System.Boolean

value = instance.SetTextFormat(UseDoc, TextFormat)
```

### C#

```csharp
System.bool SetTextFormat(
   System.bool UseDoc,
   System.object TextFormat
)
```

### C++/CLI

```cpp
System.bool SetTextFormat(
   System.bool UseDoc,
   System.Object^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True to use the default model text format, false to use a local text format
- `TextFormat`: Local [text format](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) to use if UseDoc is false

### Return Value

True if the text format was successfully set, false if not

## VBA Syntax

See [SketchText::SetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~SketchText~SetTextFormat.html).

## Remarks

To set the text format, you must be editing the sketch. See [IModelDoc2::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditSketch.html) or [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html).

To change the text format of an existing sketch text, get the [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object using [ISketchText::GetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~GetTextFormat.html) or [ISketchText::IGetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~IGetTextFormat.html), next use the various ITextFormat APIs to set the text format properties to what you want the sketch text to look like. Then use this method to change how the sketch text looks. To make the sketch text use the default model text format, use this method with the useDoc argument set to True.

To determine if this sketch text is using the default model text format or not, use [ISketchText::GetUseDocTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~GetUseDocTextFormat.html).

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~ISetTextFormat.html)
[ISketchText::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

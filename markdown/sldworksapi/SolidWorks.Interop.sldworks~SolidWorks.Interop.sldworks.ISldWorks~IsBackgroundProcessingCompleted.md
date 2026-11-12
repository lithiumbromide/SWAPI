---
title: "IsBackgroundProcessingCompleted Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IsBackgroundProcessingCompleted"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted.html"
---

# IsBackgroundProcessingCompleted Method (ISldWorks)

Gets whether SOLIDWORKS has finished background processing a drawing document that requires a lot of CPU time to open.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBackgroundProcessingCompleted( _
   ByVal FilePath As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePath As System.String
Dim value As System.Boolean

value = instance.IsBackgroundProcessingCompleted(FilePath)
```

### C#

```csharp
System.bool IsBackgroundProcessingCompleted(
   System.string FilePath
)
```

### C++/CLI

```cpp
System.bool IsBackgroundProcessingCompleted(
   System.String^ FilePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePath`: Fully qualified path and filename of the drawing document that was opened in a background process

### Return Value

True if background processing is finished, false if not

## VBA Syntax

See [SldWorks::IsBackgroundProcessingCompleted](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IsBackgroundProcessingCompleted.html).

## Remarks

SOLIDWORKS recommends that you only use this method with [ISldWorks::EnableBackgroundProcessing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.html) and [IDrawingDoc::BackgroundProcessingOption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~BackgroundProcessingOption.html) when you can quickly open a drawing document via the user interface, but that same drawing takes significantly more time to open programmatically.

To more efficiently and programmatically open a drawing document that requires a lot of CPU time and no user input:

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

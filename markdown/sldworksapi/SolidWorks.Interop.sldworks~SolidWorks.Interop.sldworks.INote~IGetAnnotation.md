---
title: "IGetAnnotation Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAnnotation.html"
---

# IGetAnnotation Method (INote)

Gets the annotation for this specific note.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As Annotation

value = instance.IGetAnnotation()
```

### C#

```csharp
Annotation IGetAnnotation()
```

### C++/CLI

```cpp
Annotation^ IGetAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [Note::IGetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~Note~IGetAnnotation.html).

## Remarks

This method obtains the owning [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object for this [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) object. The IAnnotation object is a higher-level object that contains methods that are general to all types of annotations.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAnnotation.html)

## Availability

SOLIDWORKS 99, datecode 1999207

---
title: "CheckSpelling Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "CheckSpelling"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CheckSpelling.html"
---

# CheckSpelling Method (IAnnotation)

Spell checks the text in this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function CheckSpelling( _
   ByVal Options As System.Integer, _
   ByVal Dictionary As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Options As System.Integer
Dim Dictionary As System.String
Dim value As System.Object

value = instance.CheckSpelling(Options, Dictionary)
```

### C#

```csharp
System.object CheckSpelling(
   System.int Options,
   System.string Dictionary
)
```

### C++/CLI

```cpp
System.Object^ CheckSpelling(
   System.int Options,
   System.String^ Dictionary
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Spell-check options as defined in [swCheckSpellingOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCheckSpellingOptions_e.html)
- `Dictionary`: Full path and filename of user dictionary to use (see **Remarks**)

### Return Value

Array of the misspelled words in this annotation

## VBA Syntax

See [Annotation::CheckSpelling](ms-its:sldworksapivb6.chm::/sldworks~Annotation~CheckSpelling.html).

## Remarks

The SOLIDWORKS spell checker always uses a main dictionary, which is language specific. Use the Dictionary argument to specify an additional dictionary. If Dictionary is left blank, then no additional user dictionary is used.

You can also specify additional custom dictionaries by adding them in the appropriate location in the SOLIDWORKS registry.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15

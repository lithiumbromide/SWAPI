---
title: "GetDocumentDependencies2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetDocumentDependencies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.html"
---

# GetDocumentDependencies2 Method (ISldWorks)

Gets all of the model dependencies for a document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocumentDependencies2( _
   ByVal Document As System.String, _
   ByVal Traverseflag As System.Boolean, _
   ByVal Searchflag As System.Boolean, _
   ByVal AddReadOnlyInfo As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Document As System.String
Dim Traverseflag As System.Boolean
Dim Searchflag As System.Boolean
Dim AddReadOnlyInfo As System.Boolean
Dim value As System.Object

value = instance.GetDocumentDependencies2(Document, Traverseflag, Searchflag, AddReadOnlyInfo)
```

### C#

```csharp
System.object GetDocumentDependencies2(
   System.string Document,
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

### C++/CLI

```cpp
System.Object^ GetDocumentDependencies2(
   System.String^ Document,
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Document`: Name of the document
- `Traverseflag`: True if you want to traverse down into all dependent files, false if you want only the highest level within the dependencies
- `Searchflag`: Set this argument to True if you want to use the search rules to find dependencies, false looks where the documents were last saved
- `AddReadOnlyInfo`: True if you wish to have read-only information with the filenames; false if not

### Return Value

Array of strings with two strings for each document returned in this list of dependent files:

- File name
- Filename with the complete pathname; this combination repeats itself for each dependent file found for this document

## VBA Syntax

See [SldWorks::GetDocumentDependencies2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetDocumentDependencies2.html).

## Examples

[Get Dependencies for Open and Unopened Documents (VBA)](Get_Dependencies_for_Open_and_Unopened_Documents_Example_VB.htm)
[Copy Document and Its Dependencies (VBA)](Copy_Document_and_Its_Dependencies_Example_VB.htm)
[Copy Document and Its Dependencies (VB.NET)](Copy_Document_and_Its_Dependencies_Example_VBNET.htm)
[Copy Document and Its Dependencies (C#)](Copy_Document_and_Its_Dependencies_Example_CSharp.htm)

## Remarks

As an example, calling this method on a drawing document returns a list of all the part and assemblies used in the drawing. If you set the Traverseflag to True, then each of the parts within the assembly file are also returned in this array of strings.

Another example would be calling this method with a derived mirror part. Because a derived mirror part is generated from another part, the list of model dependencies returned by this method would include the original part used to generate the derived mirror part.

Be aware that Library features are completely unassociated. They do not require the library nor do they update when changes are made to the Library feature. Therefore, this method would not return Library features.

If you use this method with an assembly that contains two documents, Part1 and SubAssem1, an example of what might be returned is:

[ "Part1", "C:\temp\Part1.SLDPRT", "SubAssem1", "c:\temp\SubAssem1.SLDASM" ]

If Traverseflag is set to True, then all of the documents contained in SubAssem1.ASM are also returned. Suppressed components are recognized and returned by this method as a dependent file.

If the AddReadOnlyInfo flag is set to True, then a string of "Read-Only" is added to the list of strings. If Part1 from were read-only, then the resulting set of strings would be:

[ "Part1", "C:\temp\Part1.SLDPRT", "Read-Only", "SubAssem1", "c:\temp\SubAssem1.SLDASM", "" ]

NOTE: If the SearchFlag is set to True, then the current directory is set to the directory of the document file. This replicates the interactive behavior of the References button in the File Open dialog window.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.html)
[ISldWorks::IGetDocumentDependenciesCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependenciesCount2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

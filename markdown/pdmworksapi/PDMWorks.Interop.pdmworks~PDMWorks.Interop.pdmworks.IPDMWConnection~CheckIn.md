---
title: "CheckIn Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "CheckIn"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CheckIn.html"
---

# CheckIn Method (IPDMWConnection)

Checks the specified closed document into the vault.

## Syntax

### Visual Basic (Declaration)

```vb
Function CheckIn( _
   ByVal filename As System.String, _
   ByVal project As System.String, _
   ByVal Number As System.String, _
   ByVal Description As System.String, _
   ByVal note As System.String, _
   ByVal i_revOption As PDMWRevisionOptionType, _
   ByVal Revision As System.String, _
   ByVal lifecycle As System.String, _
   ByVal RetainOwnership As System.Boolean, _
   ByVal References As System.Object _
) As PDMWDocument
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim filename As System.String
Dim project As System.String
Dim Number As System.String
Dim Description As System.String
Dim note As System.String
Dim i_revOption As PDMWRevisionOptionType
Dim Revision As System.String
Dim lifecycle As System.String
Dim RetainOwnership As System.Boolean
Dim References As System.Object
Dim value As PDMWDocument

value = instance.CheckIn(filename, project, Number, Description, note, i_revOption, Revision, lifecycle, RetainOwnership, References)
```

### C#

```csharp
PDMWDocument CheckIn(
   System.string filename,
   System.string project,
   System.string Number,
   System.string Description,
   System.string note,
   PDMWRevisionOptionType i_revOption,
   System.string Revision,
   System.string lifecycle,
   System.bool RetainOwnership,
   System.object References
)
```

### C++/CLI

```cpp
PDMWDocument^ CheckIn(
   System.String^ filename,
   System.String^ project,
   System.String^ Number,
   System.String^ Description,
   System.String^ note,
   PDMWRevisionOptionType i_revOption,
   System.String^ Revision,
   System.String^ lifecycle,
   System.bool RetainOwnership,
   System.Object^ References
)
```

### Parameters

- `filename`: Name of the closed document to check in
- `project`: Name of the project to which the document belongs
- `Number`: Document number
- `Description`: Document description
- `note`: Document notes
- `i_revOption`: Revision option as defined in [PDMWRevisionOptionType](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWRevisionOptionType.html) (see Remarks)
- `Revision`: Document revision
- `lifecycle`: Document lifecycle status
- `RetainOwnership`: True to retain ownership of the document in the vault, false to not
- `References`: Array of the full paths and filenames of any referenced documents to check in (see Remarks)

### Return Value

[IPDMWDocument](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html) object

## VBA Syntax

See [PDMWConnection::CheckIn](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~CheckIn.html).

## Remarks

The document to check in must be closed before calling this method.

**IMPORTANT**: Because this method is dependent on **pdmworks_libFNP.dll**, you must ensure that your application can find this DLL. The simplest way for your application to find **pdmworks_libFNP.dll** is to add its location to the PATH environmental variable. See [Microsoft Corp's Dynamic-Link Library Search Order](http://msdn.microsoft.com/en-us/library/windows/desktop/ms682586(v=vs.85).aspx) for details.

This method only works on computers where both the SOLIDWORKS Workgroup PDM Contributor or Addin client software and SOLIDWORKS Workgroup PDM API DLL are installed.

This method can check in multiple file types, e.g., SOLIDWORKS, eDrawings, Microsoft Word, text, bitmap, PDF, etc.; however, only SOLIDWORKS documents saved in SOLIDWORKS 99 and later are supported by this method.

You must own the document before you can check it in. See [IPDMWDocument::TakeOwnership](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~TakeOwnership.html) for details about how to take ownership of a document.

If i_revOption is set to PDMWRevisionOptionType.Other, then the revision argument is used.

| If checking in a document that references... | Then... |
| --- | --- |
| Non-Microsoft Word or Excel documents | The references argument is ignored. Instead, you must use IPDMWConnection::CheckIn to check in each referenced document individually. |
| Microsoft Word or Excel documents | The array of references is used. |

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 FCS

---
title: "InsertAttachment Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertAttachment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.html"
---

# InsertAttachment Method (IModelDocExtension)

Inserts a file as an Attachment to this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertAttachment( _
   ByVal FileName As System.String, _
   ByVal Linked As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FileName As System.String
Dim Linked As System.Boolean
Dim value As System.Boolean

value = instance.InsertAttachment(FileName, Linked)
```

### C#

```csharp
System.bool InsertAttachment(
   System.string FileName,
   System.bool Linked
)
```

### C++/CLI

```cpp
System.bool InsertAttachment(
   System.String^ FileName,
   System.bool Linked
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and filename of file to insert as an Attachment to this document
- `Linked`: True to link the document to the file, false to not

### Return Value

True if the file is inserted as an Attachment, false if not

## VBA Syntax

See [ModelDocExtension::InsertAttachment](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertAttachment.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::DeleteAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.html)
[IModelDocExtension::GetAttachmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount.html)
[IModelDocExtension::GetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.html)
[IModelDocExtension::IGetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

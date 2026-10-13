---
title: "GetAttachmentCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetAttachmentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount.html"
---

# GetAttachmentCount Method (IModelDocExtension)

Gets the number of attachments for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachmentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.GetAttachmentCount()
```

### C#

```csharp
System.int GetAttachmentCount()
```

### C++/CLI

```cpp
System.int GetAttachmentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of Attachments for this document

## VBA Syntax

See [ModelDocExtension::GetAttachmentCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetAttachmentCount.html).

## Remarks

This method is supported by SOLIDWORKS 2005 and later.

Call this method before calling [IModelDocExtension::IGetAttachments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetAttachments.html) to determine the size of the array for that method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::DeleteAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.html)
[IModelDocExtension::GetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.html)
[IModelDocExtension::InsertAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

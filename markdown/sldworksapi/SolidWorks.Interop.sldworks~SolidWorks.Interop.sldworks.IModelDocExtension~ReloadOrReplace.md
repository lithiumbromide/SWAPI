---
title: "ReloadOrReplace Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ReloadOrReplace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReloadOrReplace.html"
---

# ReloadOrReplace Method (IModelDocExtension)

Reloads or replaces this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReloadOrReplace( _
   ByVal ReadOnly As System.Boolean, _
   ByVal ReplaceFileName As System.String, _
   ByVal DiscardChanges As System.Boolean, _
   ByVal ForceReload As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ReadOnly As System.Boolean
Dim ReplaceFileName As System.String
Dim DiscardChanges As System.Boolean
Dim ForceReload As System.Boolean
Dim value As System.Integer

value = instance.ReloadOrReplace(ReadOnly, ReplaceFileName, DiscardChanges, ForceReload)
```

### C#

```csharp
System.int ReloadOrReplace(
   System.bool ReadOnly,
   System.string ReplaceFileName,
   System.bool DiscardChanges,
   System.bool ForceReload
)
```

### C++/CLI

```cpp
System.int ReloadOrReplace(
   System.bool ReadOnly,
   System.String^ ReplaceFileName,
   System.bool DiscardChanges,
   System.bool ForceReload
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `ReadOnly`: True to set the model document read-only after reload or replace, false to allow write access
- `ReplaceFileName`: Replacement model document; null or Nothing to reload the current model document
- `DiscardChanges`: True to discard changes made to the current model document, false to abort operation if the model document was changed (see**Remarks**)
- `ForceReload`: True to force the reload, false to not

### Return Value

Error codes as defined by[swComponentReloadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentReloadError_e.html)

## VBA Syntax

See

[ModelDocExtension::ReloadOrReplace](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ReloadOrReplace.html)

.

## Examples

[Reload Model (VBA)](Reload_Model_Example_VB.htm)

## Remarks

The model to reload or replace must be open in its own window frame.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

This method does not reload or replace the model if the top assembly has been opened invisibly. In that case, make the model visible by calling[IModelDoc2::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Visible.html)before calling this method.

You must call this method after calling[IModelDoc2::ForceReleaseLocks](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ForceReleaseLocks.html), which detaches a file from the file system, to re-attach a detached file to the file system. If you do not call this method after calling IModelDoc2::ForceReleaseLocks, then you will experience problems with OLE objects (e.g., design tables). Any changes made to a file while it is detached are not preserved unless you save the file to disk before calling this method. Additionally if you set this method's DiscardChanges parameter to false and you made changes to a detached file that you are attempting to re-attach to the file system, then this method will fail. DiscardChanges must be set to true to re-attach a detached file.

See[ISldWorks::CloseAndReopen](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CloseAndReopen.html)to perform a similar function with drawing documents.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IModelDocExtension::ReloadWithReferences Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReloadWithReferences.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

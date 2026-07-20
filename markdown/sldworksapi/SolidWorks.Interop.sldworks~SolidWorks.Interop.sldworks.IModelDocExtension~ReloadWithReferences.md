---
title: "ReloadWithReferences Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ReloadWithReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReloadWithReferences.html"
---

# ReloadWithReferences Method (IModelDocExtension)

Reloads this model document with the specified references.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReloadWithReferences( _
   ByVal ReadOnly As System.Boolean, _
   ByVal DiscardChanges As System.Boolean, _
   ByVal ReferencesToReload As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ReadOnly As System.Boolean
Dim DiscardChanges As System.Boolean
Dim ReferencesToReload As System.Object
Dim value As System.Integer

value = instance.ReloadWithReferences(ReadOnly, DiscardChanges, ReferencesToReload)
```

### C#

```csharp
System.int ReloadWithReferences(
   System.bool ReadOnly,
   System.bool DiscardChanges,
   System.object ReferencesToReload
)
```

### C++/CLI

```cpp
System.int ReloadWithReferences(
   System.bool ReadOnly,
   System.bool DiscardChanges,
   System.Object^ ReferencesToReload
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `ReadOnly`: True to set the model document read-only after reload or replace, false to allow write access
- `DiscardChanges`: True to discard changes made to the current model document, false to abort operation if the model document was changed (see

Remarks

)
- `ReferencesToReload`: Array of IDispatch pointers to referenced documents to reload

### Return Value

Error codes as defined by

[swComponentReloadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentReloadError_e.html)

## VBA Syntax

See

[ModelDocExtension::ReloadWithReferences](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ReloadWithReferences.html)

.

## Remarks

The model to reload or replace must be open in its own window frame.

This method:

- provides a performance improvement over

  [IModelDocExtension::ReloadOrReplace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReloadOrReplace.html)

  (when its ForceReload parameter is set to True).

- is faster because it reloads only a selection of referenced components.
- does not reload or replace the model if the top assembly has been opened invisibly. In that case, make the model visible by calling

  [IModelDoc2::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Visible.html)

  before calling this method.
- must be called after calling

  [IModelDoc2::ForceReleaseLocks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceReleaseLocks.html)

  , which detaches a file from the file system, to re-attach a detached file to the file system. If you do not call this method after calling IModelDoc2::ForceReleaseLocks, then you will experience problems with OLE objects (e.g., design tables). Any changes made to a file while it is detached are not preserved unless you save the file to disk before calling this method. Additionally if you set this method's DiscardChanges parameter to false and you made changes to a detached file that you are attempting to re-attach to the file system, then this method will fail. DiscardChanges must be set to true to re-attach a detached file.

See[ISldWorks::CloseAndReopen](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CloseAndReopen.html)to perform a similar function with drawing documents.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33

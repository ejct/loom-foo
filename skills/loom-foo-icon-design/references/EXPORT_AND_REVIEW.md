# Icon source, exports and inspection

- Obtain relevant current platform asset requirements before claiming formal conformance; targets differ between iOS/Android/macOS/web and by release, masks and adaptive layers.
- Inspect target-size **rendered pixels**. Review 16/20/24/32 px UI cases when applicable and several launcher/marketing sizes when required, but do not assume that every product uses all sizes.
- Check normal and reversed backgrounds, platform crop/mask, dark/light appearances, contrast, optical centering and recognition among competing icons.
- When generating icon size sets, verify files actually exist with the stated dimensions, channels, alpha and color profiles. File enumeration/static dimension check is not a visual readability review.
- `SOURCE_READY` means real editable source exists. `EXPORT_READY` means required formats/dimensions were generated and checked. `VISUALLY_REVIEWED` requires observing actual size renders; no assertion from tool description alone.
- For native project assets (e.g., Xcode asset catalog) verify required manifest/size semantics rather than renaming one square image to many sizes.

If image-generation produced only a single raster, do not represent it as editable SVG paths or an optically redesigned small-icon family.

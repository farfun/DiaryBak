!function (e, r) {
    "function" == typeof define && define.amd ? define(r) : "object" == typeof exports ? module.exports = r() : r()(e.lunr)
}(this, function () {
    return function (e) {
        if (void 0 === e) throw new Error("Lunr is not present. Please include / require Lunr before this script.");
        if (void 0 === e.stemmerSupport) throw new Error("Lunr stemmer support is not present. Please include / require Lunr stemmer support before this script.");
        var r, n, i;
        e.no = function () {
            this.pipeline.reset(), this.pipeline.add(e.no.trimmer, e.no.stopWordFilter, e.no.stemmer), this.searchPipeline && (this.searchPipeline.reset(), this.searchPipeline.add(e.no.stemmer))
        }, e.no.wordCharacters = "A-Za-zªºÀ-ÖØ-öø-ʸˠ-ˤᴀ-ᴥᴬ-ᵜᵢ-ᵥᵫ-ᵷᵹ-ᶾḀ-ỿⁱⁿₐ-ₜKÅℲⅎⅠ-ↈⱠ-ⱿꜢ-ꞇꞋ-ꞭꞰ-ꞷꟷ-ꟿꬰ-ꭚꭜ-ꭤﬀ-ﬆＡ-Ｚａ-ｚ", e.no.trimmer = e.trimmerSupport.generateTrimmer(e.no.wordCharacters), e.Pipeline.registerFunction(e.no.trimmer, "trimmer-no"), e.no.stemmer = (r = e.stemmerSupport.Among, n = e.stemmerSupport.SnowballProgram, i = new function () {
            var e, i,
                t = [new r("a", -1, 1), new r("e", -1, 1), new r("ede", 1, 1), new r("ande", 1, 1), new r("ende", 1, 1), new r("ane", 1, 1), new r("ene", 1, 1), new r("hetene", 6, 1), new r("erte", 1, 3), new r("en", -1, 1), new r("heten", 9, 1), new r("ar", -1, 1), new r("er", -1, 1), new r("heter", 12, 1), new r("s", -1, 2), new r("as", 14, 1), new r("es", 14, 1), new r("edes", 16, 1), new r("endes", 16, 1), new r("enes", 16, 1), new r("hetenes", 19, 1), new r("ens", 14, 1), new r("hetens", 21, 1), new r("ers", 14, 1), new r("ets", 14, 1), new r("et", -1, 1), new r("het", 25, 1), new r("ert", -1, 3), new r("ast", -1, 1)],
                o = [new r("dt", -1, -1), new r("vt", -1, -1)],
                s = [new r("leg", -1, 1), new r("eleg", 0, 1), new r("ig", -1, 1), new r("eig", 2, 1), new r("lig", 2, 1), new r("elig", 4, 1), new r("els", -1, 1), new r("lov", -1, 1), new r("elov", 7, 1), new r("slov", 7, 1), new r("hetslov", 9, 1)],
                a = [17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 128], m = [119, 125, 149, 1], l = new n;
            this.setCurrent = function (e) {
                l.setCurrent(e)
            }, this.getCurrent = function () {
                return l.getCurrent()
            }, this.stem = function () {
                var r, n, u, d, c = l.cursor;
                return function () {
                    var r, n = l.cursor + 3;
                    if (i = l.limit, 0 <= n || n <= l.limit) {
                        for (e = n; ;) {
                            if (r = l.cursor, l.in_grouping(a, 97, 248)) {
                                l.cursor = r;
                                break
                            }
                            if (r >= l.limit) return;
                            l.cursor = r + 1
                        }
                        for (; !l.out_grouping(a, 97, 248);) {
                            if (l.cursor >= l.limit) return;
                            l.cursor++
                        }
                        (i = l.cursor) < e && (i = e)
                    }
                }(), l.limit_backward = c, l.cursor = l.limit, function () {
                    var e, r, n;
                    if (l.cursor >= i && (r = l.limit_backward, l.limit_backward = i, l.ket = l.cursor, e = l.find_among_b(t, 29), l.limit_backward = r, e)) switch (l.bra = l.cursor, e) {
                        case 1:
                            l.slice_del();
                            break;
                        case 2:
                            n = l.limit - l.cursor, l.in_grouping_b(m, 98, 122) ? l.slice_del() : (l.cursor = l.limit - n, l.eq_s_b(1, "k") && l.out_grouping_b(a, 97, 248) && l.slice_del());
                            break;
                        case 3:
                            l.slice_from("er")
                    }
                }(), l.cursor = l.limit, n = l.limit - l.cursor, l.cursor >= i && (r = l.limit_backward, l.limit_backward = i, l.ket = l.cursor, l.find_among_b(o, 2) ? (l.bra = l.cursor, l.limit_backward = r, l.cursor = l.limit - n, l.cursor > l.limit_backward && (l.cursor--, l.bra = l.cursor, l.slice_del())) : l.limit_backward = r), l.cursor = l.limit, l.cursor >= i && (d = l.limit_backward, l.limit_backward = i, l.ket = l.cursor, (u = l.find_among_b(s, 11)) ? (l.bra = l.cursor, l.limit_backward = d, 1 == u && l.slice_del()) : l.limit_backward = d), !0
            }
        }, function (e) {
            return "function" == typeof e.update ? e.update(function (e) {
                return i.setCurrent(e), i.stem(), i.getCurrent()
            }) : (i.setCurrent(e), i.stem(), i.getCurrent())
        }), e.Pipeline.registerFunction(e.no.stemmer, "stemmer-no"), e.no.stopWordFilter = e.generateStopWordFilter("alle at av bare begge ble blei bli blir blitt både båe da de deg dei deim deira deires dem den denne der dere deres det dette di din disse ditt du dykk dykkar då eg ein eit eitt eller elles en enn er et ett etter for fordi fra før ha hadde han hans har hennar henne hennes her hjå ho hoe honom hoss hossen hun hva hvem hver hvilke hvilken hvis hvor hvordan hvorfor i ikke ikkje ikkje ingen ingi inkje inn inni ja jeg kan kom korleis korso kun kunne kva kvar kvarhelst kven kvi kvifor man mange me med medan meg meget mellom men mi min mine mitt mot mykje ned no noe noen noka noko nokon nokor nokre nå når og også om opp oss over på samme seg selv si si sia sidan siden sin sine sitt sjøl skal skulle slik so som som somme somt så sånn til um upp ut uten var vart varte ved vere verte vi vil ville vore vors vort vår være være vært å".split(" ")), e.Pipeline.registerFunction(e.no.stopWordFilter, "stopWordFilter-no")
    }
});